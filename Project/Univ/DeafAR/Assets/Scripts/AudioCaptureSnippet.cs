using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.MagicLeap;

public class AudioCaptureSnippet : MonoBehaviour
{
    PrivilegeRequester _privilegeRequester; // The Privilege Requester Component
    bool _isMicCaptureAllowed = false;


    public Text TextDisplay;
    private MLInputController _controller;
    private AudioSource _source;
    private bool _bumper = false;

    void Start()
    {
        /* This assumes you have the privilege requester on the same game object as this script */
        _privilegeRequester = GetComponent<PrivilegeRequester>();
        if (_privilegeRequester == null)
        {
            Debug.LogError("Missing PrivilegeRequester component");
            enabled = false;
            return;
        }
        /* Subscribe to the OnPrivileges done event */
        _privilegeRequester.OnPrivilegesDone += HandlePrivilegesDone;

        MLInput.Start();

        _controller = MLInput.GetController(MLInput.Hand.Left);
        _source = gameObject.GetComponent<AudioSource>();

        MLInput.OnControllerButtonDown += HandleControlButtonDown;

    }

    void OnDestroy()
    {
        if (_privilegeRequester != null)
        {
            _privilegeRequester.OnPrivilegesDone -= HandlePrivilegesDone;
        }
        MLInput.Stop();
        MLInput.OnControllerButtonDown -= HandleControlButtonDown;
    }
    void HandlePrivilegesDone(MLResult result)
    {
        if (!result.IsOk)
        {
            Debug.LogError("Failed to get all requested privileges. MLResult: " + result);
            enabled = false;

            if (result.Code == MLResultCode.PrivilegeDenied)
            {
                Debug.LogError("A privilege was denied");
                enabled = false;
            }
        }

        // All privileges requested were accepted and one of them was AudioCaptureMic
        foreach (MLRuntimeRequestPrivilegeId privilege in _privilegeRequester.Privileges)
        {
            if (privilege == MLRuntimeRequestPrivilegeId.AudioCaptureMic)
            {
                _isMicCaptureAllowed = true;
            }
            else
            {
                Debug.LogError("AudioCaptureMic privilege was not requested by privilege requester.");
                enabled = false;
            }
        }
    }
    public void CaptureSwitch()
    {
        if (_bumper)
        {
            _source.Stop();
            _source.clip = Microphone.Start(Microphone.devices[0], true, 10, 48000);
            TextDisplay.text = "Recording";
        }
        else
        {
            Microphone.End(Microphone.devices[0]);
            _source.Play();
            TextDisplay.text = "Playing";
        }
    }

    private void HandleControlButtonDown(byte controlId,
                                         MLInputControllerButton button)
    {
        if (button == MLInputControllerButton.Bumper)
        {
            _bumper = !_bumper;
            CaptureSwitch();
        }
    }
}