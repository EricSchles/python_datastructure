class KeyValue:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        return self.key+":"+str(self.value)

class HashTable:
    def __init__(self,size):
        self.size = size
        self.listing = [[] for i in xrange(self.size)]

    def getValue(self,key):
        hashed_value = hash( key ) % self.size
        bucket = self.listing[hashed_value]
        for key_value in bucket:
            if key_value.key == key:
                return key_value.value

    def setValue(self,key,value):
        hashed_value = hash( key ) % self.size
        self.listing[hashed_value].append( KeyValue( key, value ) )

htable = HashTable(10)
htable.setValue("hello","5")
htable.setValue("thing","7")
print htable.getValue("hello")
print htable.getValue("thing")
