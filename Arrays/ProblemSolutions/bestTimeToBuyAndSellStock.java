import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {
        int low = prices[0];
        int profit = 0;
        
        for(int i=1;i<=prices.length-1;i++){
            if(prices[i]>low)
                profit = Math.max(profit, prices[i]-low);
            else
                low = prices[i];
        }
        return profit;
    }
}

// Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
