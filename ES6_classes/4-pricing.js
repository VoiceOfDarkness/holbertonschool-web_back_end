/* eslint-disable */

import Currency from './3-currency';


export default class Pricing {
    constructor(price, currency) {
        this.price = price;
        this.currency = currency;
    }

    displayFullPrice() {
        return `${this.price} - ${this.currency.displayFullCurrency()}`;
    }

    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}