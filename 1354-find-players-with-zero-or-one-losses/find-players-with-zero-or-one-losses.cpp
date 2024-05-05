class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> losses;
        // Process each match
        for (const auto& match : matches) {
            int winner = match[0];
            int loser = match[1];

            // Record or update the winner's and loser's losses
            if (losses.find(winner) == losses.end()) {
                losses[winner] = 0;
            }
            if (losses.find(loser) == losses.end()) {
                losses[loser] = 1;
            } 
            else {
                losses[loser]++;
            }
        }

        vector<int> no_losses, one_loss;

        // Collect players based on their losses
        for (const auto& [player, loss_count] : losses) {
            if (loss_count == 0) {
                no_losses.push_back(player);
            } else if (loss_count == 1) {
                one_loss.push_back(player);
            }
        }

        // Sort the results
        sort(no_losses.begin(), no_losses.end());
        sort(one_loss.begin(), one_loss.end());

        return {no_losses, one_loss};
    }
};