import random

# 打开文件并读取每一行
with open('words5000.txt', 'r') as f:
    lines = f.readlines()

# 将每一行读取为字符串数组中的一项
words = [line.strip() for line in lines]

# 打印字符串数组
print(len(words))


status = 'go'
while status != 'end':
    # 从单词列表中随机选取一个单词
    chosen_word = random.choice(words)

    # 初始化隐藏版的单词，所有字母都显示为 *
    hidden_word = "*" * len(chosen_word)
    hidden_word_array = list(hidden_word)
    remainCount = len(chosen_word)
    # 循环11次让用户猜字母
    for i in range(11):
        # 打印隐藏版的单词，只显示用户猜测过的字母
        print("Hidden word:", ''.join(hidden_word_array))

        # 提示用户猜一个字母
        guess = input("\nGuess a letter, step " + str(i+1) + ": ")
        if (guess == 'end')
            break
        while len(guess.strip()) != 1 or ord(guess.strip()[0]) < 97 or ord(guess.strip()[0]) > 122:
            print("Please input a single lower case letter.")
            guess = input("Guess a letter: ").strip()

        guess = guess.strip()
        # 检查猜测的字母是否在单词中出现过
        if guess in chosen_word:
            # 将猜测的字母在隐藏版的单词中替换为字母
            for j in range(len(chosen_word)):
                if chosen_word[j] == guess[0] and hidden_word_array[j] == '*':
                    hidden_word_array[j] = guess[0]
                    remainCount = remainCount - 1

        if remainCount == 0:
            print("You won in " + str(i+1) + " steps, the word is: ", chosen_word)
            break

    # 循环结束后，打印出正确的单词和隐藏版的单词
    if remainCount > 0:
        print("You lose the game. The word is:", chosen_word)
    
    if (guess == 'end')
        break
    status = input("Press any key to continue, press end to stop")
    print("\n\n\n")
