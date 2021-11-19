# 영어 끝말잇기 (Summer/Winter Coding ~2018)

# solution2 리팩토링
def solution(n, words):
    for i in range(1, len(words)):
        # 이미 했던 단어일 경우 or 앞 단어 끝 글자와 현재 단어 첫 글자가 다를 경우 탈락
        if words[i] in words[:i] or words[i-1][-1]!=words[i][0]:
            return [i%n+1, i//n+1]      # 사람 번호, 몇 번째 차례인지
    return [0, 0]

def solution2(n, words):
    chk_list = [words[0]]
    cur_last_char = words[0][-1]
    for i in range(1, len(words)):
        # 이미 했던 단어일 경우 or 앞 단어 끝 글자와 현재 단어 첫 글자가 다를 경우 탈락
        if words[i] in chk_list or cur_last_char!=words[i][0]:
            return [i%n+1, i//n+1]      # 사람 번호, 몇 번째 차례인지
        chk_list.append(words[i])
        cur_last_char = words[i][-1]     # 끝 글자 갱신
    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))