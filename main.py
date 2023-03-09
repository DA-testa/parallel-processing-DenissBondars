# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    
    output = m * [0]
    task_time = n * [0]
    i = 0
    for j in range(m):
        output[j] = (i, task_time[i])
        task_time[i] = task_time[i] + data[j] 
        if i < n - 1:
            i = i + 1
        else:
            i = 0
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = input().split()
    n = int(n)
    m = int(m)

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = input().split()
    data = [int(i) for i in data]

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for output in result:
        print(output[0], output[1])


if __name__ == "__main__":
    main()
