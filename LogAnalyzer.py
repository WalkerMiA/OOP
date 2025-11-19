import re
import typing
#parser
with open('./logs/sfbios_logs.txt', 'r') as f:
    log_file_lines = f.readlines()



def lookup_pattern(
        pattern: str,
        lines: typing.List[str]
) -> typing.List[str]:
    match_list = []
    
    for line in lines:
        for match in re.finditer(pattern, line, re.S):
            match_text = match.group()
            match_list.append(match_text)
        
    return list(set(match_list))

properties: typing.List[str] = (
    lookup_pattern(
        pattern='(<property name="(.*?)">(.*?)<\/property>)',#(.*?) will read and print literally anything there
        lines=log_file_lines
        #ENTER A PART OF LOG FILE OR ADD A WAY TO SELECT WHAT YOU WANT TO SCAN FOR
    )
)

enabled_properties: typing.List[str] = (
    lookup_pattern(
        pattern='(<property name="(.*?)">Enabled<\/property>)',#narrows down search to have ENABLED
        lines=properties #can use previous parse or can use OG file
    )
)

