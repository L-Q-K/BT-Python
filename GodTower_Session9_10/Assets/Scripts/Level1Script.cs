using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;


public class Level1Script : MonoBehaviour {

	public Text hintText;
	public Text levelText;
	public InputField inputField;
	public Button sumbitButton;

	public string levelContent = "LEVEL";
	public string levelNumber;
	string answer;
	public string levelAnswer;
	// Use this for initialization
	void Start () {
		
		hintText.text = "Name of this place.";
		levelText.text = levelContent;
		StartCoroutine (ChangeLvTextRoutine () );
	}

	IEnumerator ChangeLvTextRoutine () {
		while (true) {
			//Wait 2 secs
			yield return new WaitForSeconds (2f);

			levelText.text = levelContent;
	
			//Wait 2 secs
			yield return new WaitForSeconds (2f);

			levelText.text = "      " + levelNumber.ToString();
		}
	}

	public void GetInput() {
		answer = inputField.text;
		check (answer);
	}

	public void check(string answer) {
		if (answer == levelAnswer) {
			hintText.text = "  Easy ha"; 

			//TODO : Change Scene:
			SceneManager.LoadScene (2);

		} else { 
			hintText.text = " So Stupid ";
			hintText.color = Color.red;

			inputField.text = "";
			inputField.ActivateInputField ();
		}
	}

	// Update is called once per frame
	void Update () {
	}
}
