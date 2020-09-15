#include <limits.h>

int myAtoi(char * str){
    int ans = 0;
    int sign = 1;
    int i = 0;
    
    while (str[i] == ' '){
        i++;
    }
    
    if (str[i] == '-' || str[i] == '+'){
        if (str[i] == '-') sign *= -1;
        i++;
    }
    
    while ('0' <= str[i] && str[i] <= '9'){

        // overflow processing
        if ((sign == -1 && ans > INT_MAX / 10) || (sign == -1 && ans == INT_MAX / 10 && str[i] - '0' > INT_MAX % 10)){
            return INT_MIN;
        }else if ((sign == 1 && ans > INT_MAX / 10) || (sign == 1 && ans == INT_MAX / 10 && str[i] - '0' > INT_MAX % 10)){
            return INT_MAX;
        }

        ans *= 10;
        ans += str[i] - '0';
        i++;
    }
    
    return ans * sign;
}