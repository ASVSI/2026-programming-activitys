"use client";

import { useEffect, useState } from "react";
import { ethers } from "ethers";
import Counter from "@/contracts/Counter.json";

export default function Home() {
  const [account, setAccount] = useState<string | null>(null);
  const [contract, setContract] = useState<ethers.Contract | null>(null);
  const [input, setInput] = useState("");
  const [number, setNumber] = useState<string>("");

  
  // Connect wallet
  const connectWallet = async () => {
    
    if (!window.ethereum) {
      alert("MetaMask not installed");
      return;
    }

    const provider = new ethers.BrowserProvider(window.ethereum);
    const signer = await provider.getSigner();
    const address = await signer.getAddress();

    const counterContract = new ethers.Contract(
      Counter.address,
      Counter.abi,
      signer
    );

    setAccount(address);
    setContract(counterContract);
  };

  // Read number
  const fetchNumber = async () => {
    if (!contract) return;
    const value = await contract.number();
    setNumber(value.toString());
  };

  // Set number
  const setNewNumber = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!contract) return;

    const tx = await contract.setNumber(input);
    await tx.wait();
    fetchNumber();
  };

  // Increment
  const increment = async () => {
    if (!contract) return;

    const tx = await contract.increment();
    await tx.wait();
    fetchNumber();
  };

  return (
    <div style={{ padding: 20 }}>
      {!account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <p>Connected: {account}</p>
      )}

      <form onSubmit={setNewNumber}>
        <input
          type="number"
          placeholder="Enter Number"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">Set Number</button>
      </form>

      <button onClick={increment}>Increment</button>
      <button onClick={fetchNumber}>View Number</button>

      {number && <p>Current Number: {number}</p>}
    </div>
  );
}
