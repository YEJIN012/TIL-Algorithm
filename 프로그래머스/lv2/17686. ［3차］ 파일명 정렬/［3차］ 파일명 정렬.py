def solution(files):
    n = int(len(files))
    
    sortfiles = [0] * n
    for i in range(n)  :
        H = ''
        N = ''
        n_flag = 0
        for j in range(len(files[i])) :
            if files[i][j].isdigit() :
                N += files[i][j]
                n_flag = 1
            elif not n_flag :
                H += files[i][j].lower()
            else :
                break
        sortfiles[i] = [H,int(N),i]

    
    # 정렬순서 : HEAD -> NUMBER -> 기존순서
    sortfiles = sorted(sortfiles, key=lambda x:(x[0],x[1],[-1]))
                    
    answer = [files[k[-1]] for k in sortfiles]

    return answer