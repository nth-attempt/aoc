inp1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
inp2 = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
inp3 = """nppdvjthqldpwncqszvftbrmjlhg"""
inp4 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
inp5 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

# Part 1
def find_packet_pos(inp):
    start = 0
    for end in range(len(inp)):
        if end >= 3:
            if len(set(inp[start:end+1])) == 4:
                return end + 1
            start += 1            

print(find_packet_pos(inp1))
print(find_packet_pos(inp2))
print(find_packet_pos(inp3))
print(find_packet_pos(inp4))
print(find_packet_pos(inp5))

# Part 2
def find_msg_pos(inp):
    start = 0
    for end in range(len(inp)):
        if end >= 13:
            if len(set(inp[start:end+1])) == 14:
                return end + 1
            start += 1 

print(find_msg_pos(inp1))
print(find_msg_pos(inp2))
print(find_msg_pos(inp3))
print(find_msg_pos(inp4))
print(find_msg_pos(inp5))
