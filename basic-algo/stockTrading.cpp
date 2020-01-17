class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;        
        int nums = prices.size();
        
        if(nums<2) return(0);
        
        int bought = -1; // Assuming the price is alway non-negative.       
        for(int k=0; k<nums-1; k++){
            // Whether to buy
            if((prices[k] < prices[k+1])&&(bought<0)){
                bought = prices[k];
            }
            // Whether to sell
            // NOTE: It is impossible to sell in the first day.
            if((prices[k] >= prices[k+1])&&(bought>=0)){
                profit += prices[k] - bought;
                bought = -1;
            }
        }
        
        // The last day.
        if(bought >=0){
                profit += prices[nums-1] - bought;
                bought = -1;            
        }
        return(profit);
    }
};

/*
买卖股票的最佳时机 II
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
*/