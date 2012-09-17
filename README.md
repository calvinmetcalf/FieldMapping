Field Mapping
============

Because the arcpy field map(ings) object was pissing me off.  Works for 10.0 api as follows

import the module

    import fm
    myMap = fm.fieldMap(featureClassOrTable[, optionalSecondThing])
        #make a field map, technically both are optional
    myMap = fm.addFC(featureClass)
        #add a new feature class, hopefully won't need this
    myMap.getMap() #returns the map
    myMap.renameField(oldFieldName,newFieldName) #renames a field
    myMap.rmPre(prefix)
        #removes a prefix, aka prefixName and prefixOthername 
        #become Name and Othername, but noprefixName stats as is
    myMap.getFieldNames()
        #returns a list of dictionaries of the form
        #{"outField":outputFieldName,"inField":inputFieldNames}
    myMap.getInFieldName(outField[, index])
        #gets the input name from the output name defaults to first field
    
api and whatnot is currently based on what I need to do for myself