import Image from "next/image"

const fetchPokemon = async (id) => {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)  
    return response.json()
}


const CreatePokemon = async () => {



    for (let i = 1; i <= 9 ; i++) {
    let posts = await fetchPokemon(i)
    console.log(posts)

        return <>
            <h1>{posts.name}</h1>
            <h1>{posts.id}</h1>
         <Image src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${posts.id}.png/`} width={150} height={150} />
    </>
    }
      }
;

export default CreatePokemon;