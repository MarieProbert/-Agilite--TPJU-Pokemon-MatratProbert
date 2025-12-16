public class Pokeball
{
    private Pokemon pokemon;
    private int prix;

    /** Constructeur quand on a pas encore le pokemon**/
    public Pokeball(int prix)
    {
        this.prix = prix;
        this.pokemon = null;
    }
    /** Constructeur quand on a déjà le pokemon**/
    public Pokeball(int prix, Pokemon pokemon){
        this.prix = prix;
        this.pokemon = pokemon;
    }

    /** Retourne le pokémon contenu dans la pokéball */
    public Pokemon getPokemon() {
        return pokemon;
    }

    /** Retourne le prix de la pokéball */
    public int getPrix() {
        return prix;
    }

    /** Modifie le pokémon à l'intérieur */
    public void setPokemon(Pokemon pokemon) {
        this.pokemon = pokemon;
    }

    /** Modifie le prix */
    public void setPrix(int prix) {
        this.prix = prix;
    }
    
    public String afficherTypePokemon() {
        if (this.pokemon == null) {
            return "Cette Pokeball est vide. Aucun type à afficher.";
        }

        String type1 = this.pokemon.getType1();
        String type2 = this.pokemon.getType2();

        if (type1 != null && type2 != null) {
            return "De types " + type1 + " et " + type2 + ".";
            
        } else if (type1 != null) {
            return "De type " + type1 + ".";
            
        } else {
            return "Le Pokémon dans cette Pokeball n'a pas de type défini.";
        }
    }
}