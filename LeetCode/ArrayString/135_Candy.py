class Solution:
    def candy(self, ratings: List[int]) -> int:
        cumulative_candy_count = 1
        current_candy_count = 1
        index_count_to_increase = 0
    
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                current_candy_count += 1
                index_count_to_increase += 1
                cumulative_candy_count += current_candy_count
            elif ratings[i] == ratings[i-1]:
                current_candy_count -= 1
                cumulative_candy_count += current_candy_count
            elif ratings[i] < ratings[i-1]:
                if current_candy_count <= 1:
                    current_candy_count = 1
                    cumulative_candy_count = cumulative_candy_count + current_candy_count + index_count_to_increase
                    if i == 1:
                        cumulative_candy_count += 1
                else:
                    current_candy_count = 1
                    cumulative_candy_count += current_candy_count
                index_count_to_increase += 1



        return cumulative_candy_count

