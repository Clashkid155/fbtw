// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.14;

contract T {
    function fund() public payable {
        require(msg.value >= 10 ether, "10 ether");
    }
}
