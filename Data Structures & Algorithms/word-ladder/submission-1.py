class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        count = 1
        q = deque([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for c in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:c] + ch + word[c+1:]
                        if newWord == endWord:
                            return count + 1
                        if newWord in wordSet:
                            wordSet.remove(newWord)
                            q.append(newWord)
            count+=1

        return 0

        
        