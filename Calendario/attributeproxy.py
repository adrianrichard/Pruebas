#!/usr/bin/python3
"""
=====================================================================================
attributeproxy.py: provide defaults and optional warnings for missings attributes in
a wrapped object; used by frigcal [1.2] for configs module settings; separate module,
as it may be a useful elsewhere; see end of this file for expected usage patterns;
=====================================================================================
"""

class AttributeProxy:
    """
    provide a default for any object's attribute that is missing;
    catches and delegates all attribute fetches/sets to wrapped object;
    """
    __trace = False  # becomes _AttributeProxy__trace
    
    def __init__(self, wrappedobject, defaultvalue=None, warnof=False):
        """
        skip my own __setattr__ here
        """
        object.__setattr__(self, '_wrappedobject', wrappedobject)
        object.__setattr__(self, '_defaultvalue',  defaultvalue)
        object.__setattr__(self, '_warnof',        warnof)
        
    def __getattr__(self, name):
        """
        on self.name for undefined name
        doesn't recur for self._X or __X: defined
        """
        if self.__trace: print('getattr', name)
        if self._warnof and not hasattr(self._wrappedobject, name):
            self.__warning(name)
        return getattr(self._wrappedobject, name, self._defaultvalue)

    def __setattr__(self, name, value):
        """
        on self.name=value for all names
        pass all other sets to wrapped object
        """
        if self.__trace: print('setattr', name, value)
        setattr(self._wrappedobject, name, value)

    def __warning(self, name):
        """
        issue warning no missing attribute if enabled;
        include type and object type names if present [1.2.3]
        """
        wrapped = self._wrappedobject
        print('Warning: %s %s missing attribute "%s"' %
                  (getattr(type(wrapped), '__name__', 'unknown'),
                   getattr(wrapped, '__name__', 'object'),
                   name), end='; ')
        print('using default: %r' % self._defaultvalue)


if __name__ == '__main__':
    # self-test if run: no output before 'Finished' means tests passed
    import sys, io
    sys.stdout = io.StringIO()   # capture prints

    class C: a=1
    i = C()
    pC = AttributeProxy(C, warnof=True)    # wrap class
    pi = AttributeProxy(i, 'dflt', True)   # wrap instance
    
    import attributeproxy as m             # import, not run
    pm = AttributeProxy(m, warnof=True)    # wrap module

    assert pC.a == 1 and pC.x == None
    assert pi.a == 1 and pi.x == 'dflt'
    assert pm.x == None
    
    assert sys.stdout.getvalue() == (
    "Warning: type C missing attribute \"x\"; using default: None\n"
    "Warning: C object missing attribute \"x\"; using default: 'dflt'\n"
    "Warning: module attributeproxy missing attribute \"x\"; using default: None\n")

    sys.stderr.write('Finished\n')
    if sys.platform.startswith('win'):
        sys.stderr.write('Press Enter\n'); input()  # keep open if clicked


"""
=====================================================================================
Usage patterns:

# module norm
>>> from attributeproxy import AttributeProxy
>>> import frigcal_configs as m
>>> m.clickmode
'mouse'
>>> m.x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'x'

# module wrapped
>>> p = AttributeProxy(m)     # default None, no warning
>>> p.clickmode
'mouse'
>>> p.x
>>> p = AttributeProxy(m, defaultvalue=True)
>>> p.x
True
>>> p = AttributeProxy(m, defaultvalue='missing', warnof=True)
>>> p.x
Warning: module frigcal_configs missing attribute "x"; using default: 'missing'
'missing'

# built-ins
>>> q = AttributeProxy([1], 99, True)
>>> q.sort
<built-in method sort of list object at 0x000000000289C448>
>>> q.nonesuch
Warning: list object missing attribute "nonesuch"; using default: 99
99
>>> q = AttributeProxy(99, 1, True)
>>> q.nonesuch
Warning: int object missing attribute "nonesuch"; using default: 1
1

# class, instance
>>> class C: a=1
...
>>> q = AttributeProxy(C, 'absent', True)
>>> q.a
1
>>> q.x
Warning: type C missing attribute "x"; using default: 'absent'
'absent'
>>> q = AttributeProxy(C(), 'absent', True)
>>> q.a
1
>>> q.x
Warning: C object missing attribute "x"; using default: 'absent'
'absent'
=====================================================================================
"""
