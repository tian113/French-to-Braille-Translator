#part 3
import doctest


def ostring_to_raisedpos(s):
    ''' (str) -> str
    Convert a braille letter represented by '##\n##\n##' o-string format
    to raised position format. 
    Braille cell dot position numbers:
    1 .. 4
    2 .. 5
    3 .. 6
    7 .. 8 (optional)

    >>> ostring_to_raisedpos('..\\n..\\n..')
    ''
    >>> ostring_to_raisedpos('oo\\noo\\noo')
    '142536'
    >>> ostring_to_raisedpos('o.\\noo\\n..')
    '125'
    >>> ostring_to_raisedpos('o.\\noo\\n..\\n.o')
    '1258'
    '''
    res = ''
    inds = [1, 4, 2, 5, 3, 6, 7, 8]
    s = s.replace('\n', '')
    for i, c in enumerate(s):
        if c == 'o':
            res += str(inds[i])
    return res 


def raisedpos_to_binary(s):
    ''' (str) -> str
    Convert a string representing a braille character in raised-position
    representation  into the binary representation.

    >>> raisedpos_to_binary('')
    '00000000'
    >>> raisedpos_to_binary('142536')
    '11111100'
    >>> raisedpos_to_binary('14253678')
    '11111111'
    >>> raisedpos_to_binary('123')
    '11100000'
    >>> raisedpos_to_binary('125')
    '11001000'
    >>> raisedpos_to_binary('278')
    '01000011'
    '''
    res=['0','0','0','0','0','0','0','0']
    #when s is ''
    
    for c in s:
        if (c==''):
            return ''.join(res)
            #converts res into a string
        
        else:
            res[int(c)-1]='1'
            #replace 0 with 1 at specific indexes indicated
            
    return ''.join(res)
    #returns the new res into string
   

def binary_to_hex(s):
    '''(str) -> str
    Convert a Braille character represented by an 8-bit binary string
    to a string representing a hexadecimal number.

    >>> binary_to_hex('00000000')
    '2800'
    >>> binary_to_hex('11111100')
    '283f'
    >>> binary_to_hex('11111111')
    '28ff'
    >>> binary_to_hex('11001000')
    '2813'
    >>> binary_to_hex('10100000')
    '2805'
    '''
    s_reverse=s[::-1]
    #reverse the given string
    
    s_decimal=int(s_reverse,2)
    #convert the string into decimal ints
    
    res_decimal=int('2800',16)
    #convert the "0" 8-bit binary(string) into decimal ints
    
    decimal_braille=res_decimal+s_decimal
    #this is the decimal number of the braille
    
    hex_braille=hex(decimal_braille)[2:]
    #this converts decimal string into hex
     
    return hex_braille


def hex_to_unicode(n):
    '''(str) -> str
    Convert a braille character represented by a hexadecimal number
    into the appropriate unicode character.

    >>> hex_to_unicode('2800')
    '⠀'
    >>> hex_to_unicode('2813')
    '⠓'
    >>> hex_to_unicode('2888')
    '⢈'
    '''
    return chr(int(str(n),16))


def is_ostring(s):
    '''(str) -> bool
    Is s formatted like an o-string? It can be 6-dot or 8-dot.

    >>> is_ostring('o.\\noo\\n..')
    True
    >>> is_ostring('o.\\noo\\n..\\noo')
    True
    >>> is_ostring('o.\\n00\\n..\\noo')
    False
    >>> is_ostring('o.\\noo')
    False
    >>> is_ostring('o.o\\no\\n..')
    False
    >>> is_ostring('o.\\noo\\n..\\noo\\noo')
    False
    >>> is_ostring('\\n')
    False
    >>> is_ostring('A')
    False
    '''
    m=s.replace('\n','1')
    #To make \n less confusing, replace them to '1'.
    
    for c in m:
        
        if ((m.count('1')!=2) and (m.count('1')!=3)):
            return False

        if (len(m)!=8 and len(m)!=11):
            return False

        if (c!='o' and c!='.' and c!='1'):
            return False

        if (m[2]!='1' or m[5]!='1'):
            return False

        if (len(m)==11 and m[8]!='1'):
            return False
        
    return True


def ostring_to_unicode(s):
    '''
    (str) -> str
    If s is a Braille cell in o-string format, convert it to unicode.
    Else return s.

    >>> ostring_to_unicode('o.\\noo\\n..')
    '⠓'
    >>> ostring_to_unicode('o.\\no.\\no.\\noo')
    '⣇'
    >>> ostring_to_unicode('oo\\noo\\noo\\noo')
    '⣿'
    >>> ostring_to_unicode('oo\\noo\\noo')
    '⠿'
    >>> ostring_to_unicode('..\\n..\\n..')
    '⠀'
    >>> ostring_to_unicode('a')
    'a'
    >>> ostring_to_unicode('\\n')
    '\\n'
    >>> ostring_to_unicode('o.\\no.\\n..\\n..')
    '⠃'
    '''
    if (is_ostring(s)):
        binary_value = raisedpos_to_binary(ostring_to_raisedpos(s))
        
        unicode_value = hex_to_unicode(binary_to_hex(binary_value))
        
        return unicode_value
    
    else:
        return s


if __name__ == '__main__':
    doctest.testmod()
