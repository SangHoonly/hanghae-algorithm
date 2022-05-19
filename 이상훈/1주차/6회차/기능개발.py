def solution(progresses, speeds):
    answer = []


    while progresses:

        for index in range(len(progresses)):
            progresses[index] += speeds[index]

        first_progress = progresses[0]
        if first_progress >= 100:
            count = 1
            for index in range(1, len(progresses)):
                if progresses[index] >= 100:
                    count += 1
                else:
                    break
            answer.append(count)
            progresses = progresses[count:]
            speeds = speeds[count:]

    return answer

