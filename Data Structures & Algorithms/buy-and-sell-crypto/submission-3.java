class Solution {
    public int maxProfit(int[] prices) {
        int mp = 0;

        int lp = 0;
        int rp = lp + 1;

        while (rp < prices.length){
            int currentProfit = prices[rp] - prices[lp];
            if (prices[rp] < prices[lp]){
                lp = rp;
                rp++;
                continue;
            }
            else{
                if (currentProfit > mp){
                    mp = currentProfit;
                }
                rp++;
            }

        }

        return mp;
    }
}