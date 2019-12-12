<?php
namespace BeerCli;

class Cli
{
    public function getStrongest($fileHandle)
    {
        $maxAlcohol=-0.1;
        while (($data = fgetcsv($fileHandle, 1000, ";")) !== false) {
            if (!empty($data[0]) && !empty($data[15]) && !empty($data[19]) && !empty($data[5])) {
                if ($maxAlcohol<floatval($data[5])) {
                    $maxAlcohol=floatval($data[5]);
                    $name=$data[0];
                    $brewery=$data[15];
                    $country=$data[19];
                }
            }
        }
        return ($name." - ".$brewery." - ".$country." - ".$maxAlcohol."\n");
    }

    public function getBitterest($fileHandle)
    {
        $maxBitterness=-0.1;
        while (($data = fgetcsv($fileHandle, 1000, ";")) !== false) {
            if (!empty($data[0]) && !empty($data[15]) && !empty($data[19]) && !empty($data[6])) {
                if ($maxBitterness<floatval($data[6])) {
                    $maxBitterness=floatval($data[6]);
                    $name=$data[0];
                    $brewery=$data[15];
                    $country=$data[19];
                }
            }
        }
        return ($name." - ".$brewery." - ".$country." - ".$maxBitterness."\n");
    }

    public function getWorldRanking($fileHandle) : array
    {
        $countBreweries=[];
        $countries=[];
        while (($data = fgetcsv($fileHandle, 1000, ";")) !== false) {
            if (!empty($data[15]) && !empty($data[19])) {
                if (!(in_array($data[19], $countries))) {
                    $countries[]=$data[19];
                    $countBreweries[$data[19]]=1;
                //Amélio : on peut use un seul tab
                } else {
                    $countBreweries[$data[19]]++;
                }
            }
        }
        arsort($countBreweries);
        return $countBreweries;
    }

    // // Il faudra clean le fichier csv car  il y a des erreurs (doublon Id, chaines vides, mauvais typage)
    // // en remplaçant les mauvaises valeurs avec par ex :
    // //
    // public function getFieldValues($fileHandle, $fieldIndex)
    // {
    //     while (($data = fgetcsv($fileHandle, 1000, ";")) !== false) {
    //         if (!empty($data[$fieldIndex])===false) {
    //             $beersArray[]="UNDEFINED";
    //         } else {
    //             $beersArray[]=$data[$fieldIndex];
    //         }
    //     }
    //     return $beersArray;
    // }

    public function openCSV($fileName)
    {
        //$fileName = "open-beer-database.csv";
        if (!file_exists($fileName)) {
            throw new \Exception('File not found.');
        } else {
            $handle = fopen($fileName, "r");
            if (!$handle) {
                throw new \Exception('File open failed.');
            }
        }
        return $handle;
    }

    public function exec($argv): void
    {
        //Contrôles à faire sur les args
        $command=$argv[1];
        $fileName=$argv[2];

        try {
            $fileHandle=$this->openCSV($fileName);
        } catch (\Exception $e) {
            // error message
        }

        //Liste des champs pour info
        // $fieldNameArray = explode(";","Name;id;brewery_id;cat_id;style_id;Alcohol By Volume;International Bitterness Units;Standard Reference Method;Universal Product Code;filepath;Description;add_user;last_mod;Style;Category;Brewer;Address;City;State;Country;Coordinates;Website");
        // $fieldNameArray=array_flip($fieldNameArray);
        // print_r($fieldNameArray);
        
        
        switch ($command) {
            case 'beer:strongest':

                echo $this->getStrongest($fileHandle);
                fclose($fileHandle);

                break;

            case 'beer:bitterest':

                echo $this->getBitterest($fileHandle);
                fclose($fileHandle);

                break;
            
            case 'beer:ranking:brewery':
                $ranking=$this->getWorldRanking($fileHandle);
                fclose($fileHandle);
                foreach ($ranking as $country => $nb_brewery) {
                    echo $nb_brewery." - ".$country."\n";
                }
                break;
            
            case 'beer:ranking:style':
                # code...
                break;
            
            case 'beer:ranking:alcohol':
                # code...
                break;

            case 'display':
                # code...
                break;

            default:
                echo("Invalid command");
                break;
        }
    }
}
