// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.14;

contract T {
     function fund() public payable returns(uint) {
        require(msg.value >= 10 ether, "Minimum fund of 10 Ether!");
        return msg.value;
    }
}
