/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    var value = val
    let object = {
        toBe : function(arg1) {
            if (value === arg1){
                return true
            }else{
                throw new Error("Not Equal");
            }
        },
        notToBe : function(arg1) {
            if (value !== arg1){
                return true
            }else{
                throw new Error("Equal");
            }
        }
    } 
    
    return object
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */