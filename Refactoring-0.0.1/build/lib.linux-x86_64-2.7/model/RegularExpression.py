import re

class RegularExpression(object):

    def __init__(self,regex_arr,test_str):
        self.regex_arr = regex_arr
        self.test_str = test_str

    def apply(self):

        for index in range(len(self.regex_arr)):

            matches = re.finditer(self.regex_arr[index], self.test_str, re.MULTILINE | re.IGNORECASE )

            for matchNum, match in enumerate(matches):
                matchNum = matchNum + 1

                s = ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                                    end=match.end(), match=match.group()))

                if match.start()==0 and match.group()!='' and match.end()>=2:
                    return self.regex_arr[index]

                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1

                    print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                                     end=match.end(groupNum),
                                                                                                    group=match.group(groupNum)))


        return "none"


