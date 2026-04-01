import { useEffect, useState } from "react";

import { HiXMark } from "react-icons/hi2";

export default function RegistrationForm({ closeFunction }) {

  const [mounted, setMounted] = useState(false);

  // render popup with initial opacity and scale set to 0 
  // upon render set mounted state to true
  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <Overlay>

      <div className={`fixed z-1 px-15 py-10 p bg-bgsecondary 
        top-1/4 flex flex-col gap-4 text-fontalt rounded-sm justify-between 
        h-110 transition-all duration-600
      ${mounted ? "scale-100 opacity-100" : "scale-80 opacity-0"}
        border-fontalt border-1`}>

        <div className="flex items-center justify-between 
          text-black font-light tracking-wide">
          <h1>JOIN BOOKMARKED</h1>
          <HiXMark className="hover:fill-red-500 w-6 h-auto cursor-pointer" onClick={closeFunction} />
        </div>

        <div className="flex flex-col gap-3">
          <InputField label={"Email Address"} placeholder={"bob@gmail.com"} />
          <InputField label={"Username"} placeholder={"booklover67"} />
          <InputField label={"Password"} placeholder={"hplovecraft123"} />
        </div>

        <button className="self-start border-green-700 border 1 bg-green-500 px-5 py-1 rounded-sm mt-1 text-white font-semibold opacity-90 hover:opacity-100">
          Sign Up
        </button>
      </div>
    </Overlay>)
}

function InputField({ label, placeholder }) {

  return (
    <div  >
      <p>{label}</p>
      <input type="text" placeholder={placeholder}
        className="bg-bgprimary focus:bg-white focus:ring-1 focus:ring-green-500 px-1 py-1 rounded-sm w-80 focus:outline-none text-black" />
    </div>

  )
}

function Overlay({ children }) {

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/30 backdrop-blur-sm">
      {children}
    </div>
  )
}
