// given: ajax(url, data, cb)

var getPerson = partial(ajax, 'http://some.api/person');
var getLastOrder = partial(ajax, 'http://some.api/order', {id: -1});

getLastOrder(function orderFound(order) {
    getPerson({id: order.personId}, function personFound(person) {
        output(person.name)
    });
});