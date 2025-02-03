/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(p1, p2) {
    return Promise.all([p1, p2])
    .then(results => results[0]+results[1]) // Won't run since p3 rejects
    .catch(error => console.log("Caught:", error));
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */