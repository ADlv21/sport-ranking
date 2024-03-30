"use client";
import Navbar from "@/components/Navbar";
import SportSelect from "@/components/SportSelect";
import { sports } from "@/lib/constants";
import React, { useState } from "react";

const Home = () => {
  const [value, setValue] = useState("");
  return (
    <div>
      <Navbar />
      <SportSelect sports={sports} value={value} setValue={setValue} />
    </div>
  );
};

export default Home;
