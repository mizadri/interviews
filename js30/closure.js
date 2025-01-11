/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var aux = n
    var first = true
    return function() {
        
        if (!first){
            aux += 1
        }else{
            first = false
        }
            
        return aux
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */