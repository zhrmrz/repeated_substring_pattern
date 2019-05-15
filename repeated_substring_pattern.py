class Sol:
    def repeated_substring_pattern(self,str):
        return str in (str[1:]+str[:-1])


if __name__ == '__main__':
    p1=Sol()
    print(p1.repeated_substring_pattern('aa'))
