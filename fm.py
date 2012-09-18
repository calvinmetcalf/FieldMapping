import arcpy

class fieldMap:
    def __init__(this,fc=None,sfc=None):
        this.m=arcpy.FieldMappings()
        if fc is not None:
            this.addFC(fc)
        if sfc is not None:
            this.addFC(sfc)
    def addFC(this,fc):
        this.m.addTable(fc)
    def renameField(this,oldF,newF):
        fIndex=this.m.findFieldMapIndex(oldF)
        fmap = this.m.getFieldMap(fIndex)
        fo=fmap.outputField
        fo.name=newF
        fmap.outputField=fo
        this.m.replaceFieldMap(fIndex,fmap)
    def rmPre(this,prefix):
        for n in range(this.m.fieldCount):
            nom =this.m.fields[n].name
            if len(nom)>len(prefix) and nom[:len(prefix)] == prefix:
                this.renameField(nom,nom[len(prefix):])
    def getMap(this):
        return this.m
    def getOutFieldNames(this):
        d=[]
        for n in range(this.m.fieldCount):
            d.append(m.fields[n].name)
        return d
    def getInFieldName(this,outF,index=0):
        return this.m.getFieldMap(this.m.findFieldMapIndex(outF)).getInputFieldName(index)
    def getFieldNames(this):
        d=[]
        outF=this.getOutFieldNames()
        for fo in outF:
            fi = this.getInFieldName(this,fo)
            d.append({"outField":fo,"inField":fi})
    def rmField(this,field):
        index=this.m.findFieldMapIndex(field)
        this.m.removeFieldMap(index)
    def mergeFields(this,target,apendix):
        tIndex = this.m.findFieldMapIndex(target)
        aIndex = this.m.findFieldMapIndex(apendix)
        tMap=this.m.getFieldMap(tIndex)
        aMap=this.m.getFieldMap(aIndex)
        tMap.addInputField(aMap.getInputTableName(0),aMap.getInputFieldName(0))
        this.m.replaceFieldMap(tIndex,tMap)
        this.m.removeFieldMap(aIndex)