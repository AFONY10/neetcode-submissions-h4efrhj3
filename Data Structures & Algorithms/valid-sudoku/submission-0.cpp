class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9), columns(9), boxes(9);

        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                char num = board[i][j];

                if(num == '.'){
                    continue;

                }

                // Check the row
                if(rows[i].count(num)){
                    return false;
                }
                rows[i].insert(num);

                // Cehck the column
                if(columns[j].count(num)){
                    return false;
                }
                columns[j].insert(num);

                // Check 3x3 sub-box
                int boxIndex = (i/3)*3+(j/3);
                if (boxes[boxIndex].count(num)) {
                    return false;
                }
                boxes[boxIndex].insert(num);
            }
        }

        return true;
    }
};
