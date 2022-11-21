class BrailleUtils():

    def label010_to_chr(label010):
        # Convert label in label010 format to unicode caracter
        v = [1,2,4,8,16,32]
        r = sum([v[i] for i in range(6) if label010[i]=='1'])
        return  chr(0x2800 + r)

    def chr_to_label010(chr):
        # Convert unicode chacter to label in label010 format
        int_lbl = ord(chr) - 0x2800
        if int_lbl >= 0 and int_lbl < 64:
            v = [1,2,4,8,16,32]
            r = ''.join([ '1' if int_lbl&v[i] else '0' for i in range(6)])
            return r

    def chr_to_label123(chr):
        int_lbl = ord(chr) - 0x2800
        v = [1,2,4,8,16,32]
        r = ''.join([ str(i+1) for i in range(6) if int_lbl&v[i]])
        return r

    def label123_to_chr(label123):
        v = [1,2,4,8,16,32]
        r = sum([v[int(ch)-1] for ch in label123])
        return  chr(0x2800 + r)

