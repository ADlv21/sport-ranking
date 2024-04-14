"use client";

import SportSelect from "@/components/SportSelect";
import { sports } from "@/lib/constants";
import React, { useState } from "react";

const Sports = () => {
    const [value, setValue] = useState("");
    return (
        <div>
            <SportSelect sports={sports} value={value} setValue={setValue} />
        </div>
    );
};

export default Sports;
