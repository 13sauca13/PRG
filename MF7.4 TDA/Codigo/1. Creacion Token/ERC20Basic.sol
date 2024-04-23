//SPDX-License-Identifier: MIT
pragma experimental ABIEncoderV2;
pragma solidity >=0.6.12 <0.9.0;

import "./IERC20.sol";
import "./SafeMath.sol";

contract ERC20Basic is IERC20 {
    string public constant name = "Saucoin";
    string public constant symbol = "SCN";
    uint public constant decimals= 2;

    using SafeMath for uint256;

    mapping(address=>uint) balances;
    mapping (address => mapping (address => uint)) allowed;
    uint256 totalSupply_;

    constructor (uint256 initialSupply) {
    totalSupply_ = initialSupply;
    balances[msg.sender]=totalSupply_;
    }

    //El suministro total de tokens
    function totalsupply() public override view returns (uint256){
        return totalSupply_;
    }
    function increaseTotalSupply(uint newTokensAmount) public {
        totalSupply_+=newTokensAmount;
        balances[msg.sender]+= newTokensAmount;
    }
    //Devuelve el número de tokens de una dirección
    function balanceOf(address tokenOwner) public override view returns (uint256){
        return balances[tokenOwner];
    }
    //Si un usuario tiene la cantidad de tokens suficientes (y devuelve el número)
    function allowance(address owner, address delegate) public override view returns (uint256){
        return allowed[owner][delegate];
    }
    //Tokens del suministro inicial a un usuario
    function transfer(address recipient, uint256 numTokens) public override returns (bool){
        require(numTokens <=balances[msg.sender]);
        balances[msg.sender]=balances[msg.sender]. sub(numTokens);
        balances[recipient]=balances[recipient].add(numTokens);
        emit Transfer(msg.sender, recipient, numTokens);
        return true;
    }
    //Si el contrato puede mandar una cantidad de tokens a un usuario
    function approve(address delegate, uint256 numTokens) public override returns (bool){
        allowed[msg.sender][delegate]=numTokens;
        emit Approval(msg.sender, delegate, numTokens);
        return true;
    }
    //Habilita la transferencia de tokens entre usuarios
    function transferFrom(address owner, address buyer, uint256 numTokens) public override returns (bool){
        require(numTokens <= balances[owner]);
        require(numTokens <= allowed[owner][msg.sender]);
        balances[owner]=balances[owner].sub(numTokens);
        allowed[owner][msg.sender]=allowed[owner][msg.sender].sub(numTokens);
        balances[buyer]=balances[buyer].add(numTokens);
        emit Transfer (owner, buyer, numTokens);
        return true;
    }
}