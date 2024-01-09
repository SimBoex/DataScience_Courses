// SPDX-License-Identifier: MIT
pragma solidity ^0.8.11;

contract Lottery {
    address payable public owner;
    address payable[] public players;

    constructor() {
        owner = payable(msg.sender);
    }

    event LotteryEntered(address indexed player);
    event WinnerPicked(address indexed winner, uint prize);


    function getPlayers() public view returns (address payable[] memory) {
        return players;
    }

    function enter() public payable {
        require(msg.value  ==  1 ether, "the fees for joining the lottery is 1 ether");
         // Check if the sender's address is not already in the players array
        for (uint i = 0; i < players.length; i++) {
            require(players[i] != payable(msg.sender), "you can't join the same  lottery twice");
        }
        // address of player entering lottery
        players.push(payable(msg.sender));
        emit LotteryEntered(msg.sender);
    }


    function getRandomNumber() public view returns (uint) {
        bytes memory nonceData = abi.encodePacked(block.timestamp, owner);    
    return uint(keccak256(nonceData));
    }


    function pickWinner() public  {
        require(msg.sender == owner, "Only the owner can pick the winner");
        uint percentageToOwner = 20;
        uint index = getRandomNumber() % players.length;
        address payable winner = players[index];
        uint totalBalance = address(this).balance;
        // Transfer percentage to the owner and the remaining to the winner
        uint tot = totalBalance * percentageToOwner / 100;
        owner.transfer(tot);
        winner.transfer(totalBalance - tot);
        emit WinnerPicked(winner, totalBalance - tot);
        // reset the state of the contract
        players = new address payable[](0);
    }


}