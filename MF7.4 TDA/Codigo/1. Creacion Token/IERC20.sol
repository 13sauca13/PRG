//SPDX-License-Identifier: MIT
pragma solidity >=0.6.12 <0.9.0;
//Interface token ERC
interface IERC20{
    //El suministro total de tokens
    function totalsupply()external view returns (uint256);
    //Devuelve el número de tokens de una dirección
    function balanceOf(address account)external view returns (uint256);
    //Si un usuario tiene la cantidad de tokens suficientes (y devuelve el número)
    function allowance(address owner, address spender)external view returns (uint256);
    //Tokens del suministro inicial a un usuario
    function transfer(address recipient, uint256 amount) external returns (bool);
    //Si el contrato puede mandar una cantidad de tokens a un usuario
    function approve(address spender, uint256 amount) external returns (bool);
    //Habilita la transferencia de tokens entre usuarios
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    //Evento número 1
    event Transfer(address indexed from, address indexed to, uint256 value);
    //Evento número 2
    event Approval(address indexed owner, address indexed spender, uint256 value);
}