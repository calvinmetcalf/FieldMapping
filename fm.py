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
        if this.m.findFieldMapIndex("OBJECTID")>=0:
            this.rmField("OBJECTID")
    def renameField(this,oldF,newF):
        fIndex=this.m.findFieldMapIndex(oldF)
        fmap = this.m.getFieldMap(fIndex)
        fo=fmap.outputField
        fo.name=newF
        fmap.outputField=fo
        this.m.replaceFieldMap(fIndex,fmap)
    def rmPre(this,prefix):
        for nom in this.getOutFieldNames():
            if len(nom)>len(prefix) and nom[:len(prefix)] == prefix:
                if nom[len(prefix):]=="OBJECTID":
                    this.rmField(nom)
                elif this.m.findFieldMapIndex(nom[len(prefix):])>=0:
                    this.mergeFields(nom[len(prefix):],nom)
                else:
                    this.renameField(nom,nom[len(prefix):])
    def getMap(this):
        return this.m
    def getOutFieldNames(this):
        d=[]
        for n in range(this.m.fieldCount):
            d.append(this.m.fields[n].name)
        return d
    def getInFieldName(this,outF,index=0):
        return this.m.getFieldMap(this.m.findFieldMapIndex(outF)).getInputFieldName(index)
    def getFieldNames(this):
        d=[]
        outF=this.getOutFieldNames()
        for fo in outF:
            fi = this.getInFieldName(fo)
            d.append({"outField":fo,"inField":fi})
        return d
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