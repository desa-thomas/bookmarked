

export default function HomePage({ loggedIn }) {
  /**
  *    HomePage Boundary Class
  *    Takes login state
  */
  return (loggedIn ? <LoggedInHomepage /> : <DefaultHomepage />)
}

function LoggedInHomepage() {

  return (
    <div>
      LOGGED IN
    </div>)
}

function DefaultHomepage() {

  return (
    <div className="border flex-1  flex flex-col items-center gap-5 pt-5">

      {/** SLOGAN / CALL TO ACTION**/}
      <div className="text-4xl font-medium font-playfair items-center flex flex-col">
        <p>Track books you've read.</p>
        <p>Save those you want to read.</p>
        <p>Tell your friends what's good.</p>
      </div>
      <SignupButton />
    </div>
  )
}

function SignupButton() {
  return (
    <button className=" p-3 border-black border-1 rounded-md"> 
    Begin Your Reading Journey </button>
  )
}
