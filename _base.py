#COPYRIGHT 2012 ESRI
#
#TRADE SECRETS: ESRI PROPRIETARY AND CONFIDENTIAL
#Unpublished material - all rights reserved under the
#Copyright Laws of the United States.
#
#For additional information, contact:
#Environmental Systems Research Institute, Inc.
#Attn: Contracts Dept
#380 New York Street
#Redlands, California, USA 92373
#
#email: contracts@esri.com
class _NamedAttrObject(object):
    """Base class for objects that should be converted into a string like: ATTR1=val1 ATTR2=val2"""
  
    @classmethod
    def _add_attr(cls, name, nameCmd, value = None, bReadonly = False):
      if not hasattr(cls, "_attr_arr") :
          cls._attr_arr = []
  
      cls._attr_arr += [[name, nameCmd]]
      setattr(cls, "__%s" % (name), value)
    
      if bReadonly :
          setattr(cls, name, property(fget=lambda instance       : cls.__propertyGetter(instance, name),
                                      fset=None))
      else :
          setattr(cls, name, property(fget=lambda instance       : cls.__propertyGetter(instance, name),
                                      fset=lambda instance, val  : cls.__propertySetter(instance, val, name)))
    
    def __propertyGetter(self, name):
        assert hasattr(self, "__%s" % name), "attribute __%s " % (name)+"is not in the " + str(type(self))
        return getattr(self, "__%s" % name)

    def __propertySetter(self, value, name):
        setattr(self, "__%s" % name, value)

    @classmethod
    def _make_readonly(cls, name):
        assert hasattr(cls, "__%s" % name), "attribute __%s " % (name)+"is not in the " + cls.__name__
        setattr(cls, name, property(fget=lambda instance       : cls.__propertyGetter(instance, name),
                                    fset=None))
        
    @classmethod
    def _make_readwrite(cls, name):
        assert hasattr(cls, "__%s" % name), "attribute __%s " % (name)+"is not in the " + cls.__name__
        setattr(cls, name, property(fget=lambda instance       : cls.__propertyGetter(instance, name),
                                    fset=lambda instance, val  : cls.__propertySetter(instance, val, name)))
    
    def __repr__(self):
        strRes = ""
        for name, nameCmd in self._attr_arr:
            value = getattr(self, name)
            if value is not None and value != "" and value != "#":
                strRes += nameCmd + "=" + str(value) + " "
        return strRes.rstrip()

    def __str__(self):
      return self.__repr__()

    @property
    def _arc_object(self):
        return str(self)

def _ValidateParameter(val, def_val):
    if val == "" or val == "#" :
        return def_val
    else :
        return val
