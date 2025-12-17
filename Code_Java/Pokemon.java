
/**
 * Décrivez votre classe Pokemon ici.
 *
 * @author Barie
 * @version 1
 */
public class Pokemon
{
    private String type1;
    private String type2;
    private Pokeball pokeball ;

    /**
     * Constructeur d'objets de classe Pokemon
     */
    public Pokemon(String type1, String type2)
    {
        this.type1 = type1 ;
        this.type2 = type2 ;
    }
    
    public Pokemon(String type1, String type2, Pokeball pokeball)
    {
        this.type1 = type1 ;
        this.type2 = type2 ;
        this.pokeball = pokeball ;
    }

    
    public String getType1()
    {
        return this.type1 ;
    }
    
    public String getType2(){
        return this.type2 ;
    }
    
    public Pokeball getPokeball(){
        return this.pokeball ;
    }
    
    public void setType1(String newType1){
        this.type1 = newType1 ;
    }
    
    public void setType2(String newType2){
        this.type2 = newType2 ;
    }
    
    public void setPokeball(Pokeball newPokeball){
        this.pokeball = newPokeball ;
    }
}