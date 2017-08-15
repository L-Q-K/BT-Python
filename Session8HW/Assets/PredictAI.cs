using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PredictAI : MonoBehaviour {

	public Text displayText;
	public InputField inputFieldMin;
	public InputField inputFieldMax;
	public Button higher;
	public Button lower;
	public Button Holy;
	public Button PABut;

	string minInp;
	string maxInp;
	int min;
	int max;
	int guessNumber; 

	public void GetInput (){

		//Get Input:
		minInp = inputFieldMin.text;
		maxInp = inputFieldMax.text;
		max = int.Parse (maxInp);
		min = int.Parse (minInp);

		if (min > max) {
			min = max;
			displayText.text = "You can't troll me ";
		}

		//Xoa Object canh 1:
		inputFieldMin.gameObject.SetActive (false); 
		inputFieldMax.gameObject.SetActive (false);

		guessNumber = Random.Range (min, max);
		displayText.text = "I'm Skynet and I will fck your mind now, think a number and let me guess, is it " + guessNumber.ToString () + " ?";

		higher.gameObject.SetActive (true);
		lower.gameObject.SetActive (true);
		Holy.gameObject.SetActive (true);
	}

	// Use this for initialization
	void Start () {
		PABut.gameObject.SetActive (false);
		higher.gameObject.SetActive (false);
		lower.gameObject.SetActive (false);
		Holy.gameObject.SetActive (false);

		displayText.text = "Enter the range your number in";
	}

	public void HigherButton(){
		if (min == max) { 
			displayText.text = "This is the number," + guessNumber.ToString () + "no way it is not, don't troll AI ";  
			higher.gameObject.SetActive (false);
			lower.gameObject.SetActive (false);
		} else {
			min = guessNumber + 1;

			guessNumber = Random.Range (min, max);

			if (guessNumber == max) {
				higher.gameObject.SetActive (false);
			}

			lower.gameObject.SetActive (true);

			displayText.text = "Is it " + guessNumber.ToString () + "?";
		}
	}
	public void LowerButton(){
		if (min == max) { 
			displayText.text = "This is the number," + guessNumber.ToString () + "no way it is not, don't troll AI ";  
			higher.gameObject.SetActive (false);
			lower.gameObject.SetActive (false);
		} else {
			max = guessNumber - 1;

			guessNumber = Random.Range (min, max);

			if (guessNumber == min) {
				lower.gameObject.SetActive (false);
			}
				
			higher.gameObject.SetActive (true);

			displayText.text = "Is it " + guessNumber.ToString () + "?";
		}
	}
	public void YesButton(){
		displayText.text = "You are stupid hooman";
		higher.gameObject.SetActive (false);
		lower.gameObject.SetActive (false);
		Holy.gameObject.SetActive (false);
		PABut.gameObject.SetActive (true);
	}
	public void playAgainButon (){
		PABut.gameObject.SetActive (false);
		inputFieldMin.gameObject.SetActive (true); 
		inputFieldMax.gameObject.SetActive (true);
		higher.gameObject.SetActive (false);
		lower.gameObject.SetActive (false);
		Holy.gameObject.SetActive (false);
	
		inputFieldMin.text = "";
		inputFieldMax.text = "";


		displayText.text = "Enter the range your number in";
	}
	// Hjx 100 lines =((
}
