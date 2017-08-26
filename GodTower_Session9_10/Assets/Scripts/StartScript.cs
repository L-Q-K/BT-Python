using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class StartScript : MonoBehaviour {

	// Use this for initialization:
	void Start () {
	}

	public void beginButton () {
		SceneManager.LoadScene (1);
	}

	public void continueButton () {
		//		Application.LoadLevel ();
	}

	// Update is called once per frame
	void Update () {

	}
}
