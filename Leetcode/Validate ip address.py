class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def validipv4(query_ip_address):
            for part in query_ip_address.split('.'):
                
                if valid_part_for_ipv4(part) and str(int(part))==part and int(part)>=0 and int(part)<=255:
                    pass
                else:
                    return False
            return True
        def valid_part_for_ipv4(part):
            if not part:
                return False
            for each_char in part:
                if each_char>='0' and each_char<='9':
                    pass
                else:
                    return False
            return True
        def valid_part_for_ipv6(part):
            part = part.lower()
            for each_char in part:
                if (each_char>='0' and each_char<='9') or ( each_char>='a' and each_char<='f'):
                    pass
                else:
                    return False
            return True
        def validipv6(query_ip_address):
            for part in query_ip_address.split(':'):
                if len(part)>=1 and len(part)<=4 and valid_part_for_ipv6(part):
                    pass
                else:
                    return False
            return True
        if queryIP.count('.')==3 and validipv4(queryIP):
            return 'IPv4'
        elif queryIP.count(':')==7 and validipv6(queryIP):
            return 'IPv6'
        return 'Neither'