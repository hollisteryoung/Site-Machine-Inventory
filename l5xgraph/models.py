class Parameter:
    def __init__(this,name,station,datatype,radix,alias_for,unit,min_value,max_value,circular,description):
        this.name = name
        this.station = station
        this.datatype = datatype
        this.radix = radix,
        this.alias_for = alias_for
        this.unit = unit
        this.min_value = min_value
        this.max_value = max_value,
        this.circular = circular,
        this.description = description

  
    def __str__(self):
        return "This object contains:\n Tag: %s \n " \
        "Station : %s \n" \
        "Unit of Measurement: %s \n" \
        "DataType: %s \n" \
        "Radix : %s \n" \
        "Alias For: %s \n" \
        "Min Value: %s \n" \
        "Max Value %s \n" \
        "Circular : %s \n" \
        "Descripition: %s \n" % (self.name,self.station,self.unit,self.datatype,self.radix,self.alias_for,self.min_value,self.max_value,self.circular,self.description)

    def __repr__(self):
        return str(self)

class Reference:
    def __init__(self,file,program,routine,rung_number,instruction,base_tag,position,is_write,literal_value):
        self.file = file
        self.program = program
        self.routine = routine
        self.rung_number = rung_number
        self.instruction = instruction
        self.base_tag = base_tag
        self.position = position
        self.is_write = is_write
        self.literal_value = literal_value




class Declaration:
    def __init__(self,name,data_type,radix,tag_type,alias_for,constant,external_access,description,scope):
        self.name = name
        self.data_type = data_type
        self.radix = radix
        self.tag_type = tag_type
        self.alias_for = alias_for
        self.constant = constant
        self.external_access = external_access
        self.description = description
        self.scope = scope
    

class Limits:
    def __init__(self,value,low,high,circular):
        self.value = value
        self.low = low
        self.high = high
        self.circular = circular
        
    