## Brute force don't expect it to work.
prime = 1000000007
n= int(input())
wine_prices = list(map(int, input().split()))
def get_max_profit(start_idx, end_idx, year):
    if end_idx<start_idx:
        return 0%prime
    if start_idx==end_idx:
        return (year*wine_prices[start_idx])%prime
    ## We must sell cheap now and be greedy.
    if wine_prices[start_idx] < wine_prices[end_idx]:
        return (year*wine_prices[start_idx]+get_max_profit(start_idx+1, end_idx, year+1))%prime
    else:
        return (year*wine_prices[end_idx]+get_max_profit(start_idx, end_idx-1, year+1))%prime
print(get_max_profit(0, len(wine_prices)-1, 1))