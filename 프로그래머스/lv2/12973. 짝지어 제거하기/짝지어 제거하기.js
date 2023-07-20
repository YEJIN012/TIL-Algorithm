function solution(s)
{
    var answer = 0;

    let stack = [];
    for (i=0; i<s.length; i++) {
        stack.length > 0 && stack.at(-1) == s[i] ? stack.pop() : stack.push(s[i])
    };
    answer = stack.length == 0 ? 1 : 0
    return answer;
}