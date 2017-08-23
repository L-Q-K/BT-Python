using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class Level3Script : MonoBehaviour {

	public Text hintText;
	public Text levelText;
	public InputField inputField;
	public Button sumbitButton;
	public Button hintButton;
	public Button backButton;
	public Image lv3Hint;
	public Image lv3Hint2;

	public string levelContent = "LEVELS";
	public string levelNumber;
	string answer;
	public string levelAnswer;
	// Use this for initialization
	void Start () {
		hintText.text = "Clock pointer will tell you.";
		backButton.gameObject.SetActive (false);
		lv3Hint2.gameObject.SetActive (false);
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
		if (answer.ToLower() == levelAnswer) {
			hintText.text = "  Easy ha"; 
			hintText.color = Color.blue;

			SceneManager.LoadScene (4) ;
		} else { 
			hintText.text = " So Stupid ";
			hintText.color = Color.red;

			inputField.text = "";
			inputField.ActivateInputField ();
		}
	}

	public void hidingHintButton () {
		hintButton.gameObject.SetActive (false);
		backButton.gameObject.SetActive (true);
		lv3Hint.gameObject.SetActive (false);
		lv3Hint2.gameObject.SetActive (true);
	}

	public void backButtonSetup () {
		hintButton.gameObject.SetActive (true);
		backButton.gameObject.SetActive (false);
		lv3Hint.gameObject.SetActive (true);
		lv3Hint2.gameObject.SetActive (false);
	}

	// Update is called once per frame
	void Update () {
	}
}
