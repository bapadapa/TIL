
namespace GoogleARCore.Examples.ObjectManipulation
{
    using System.Collections.Generic;
    using GoogleARCore;
    using UnityEngine;
    using UnityEngine.UI;
    using UnityEngine.Animations;
    public class PlaneManager : MonoBehaviour
    {
        private static PlaneManager instance = null;
        public static PlaneManager Instance
        {
            get
            {
                return instance;

            }
        }
        /// <summary>
        /// The time to delay, after ARCore loses tracking of any planes, showing the plane
        /// discovery guide.
        /// </summary>
        [Tooltip("The time to delay, after ARCore loses tracking of any planes, showing the plane " +
                 "discovery guide.")]
        public float DisplayGuideDelay = 3.0f;
        public Text te;
        /// <summary>
        /// The time to delay, after displaying the plane discovery guide, offering more detailed
        /// instructions on how to find a plane.
        /// </summary>
        [Tooltip("The time to delay, after displaying the plane discovery guide, offering more detailed " +
                 "instructions on how to find a plane.")]
        public float OfferDetailedInstructionsDelay = 8.0f;



        /// <summary>
        /// The time to delay, after Unity Start, showing the plane discovery guide.
        /// </summary>
        private const float k_OnStartDelay = 1f;

        /// <summary>
        /// The time to delay, after a at least one plane is tracked by ARCore, hiding the plane discovery guide.
        /// </summary>
        private const float k_HideGuideDelay = 0.75f;

        /// <summary>
        /// The duration of the hand animation fades.
        /// </summary>
        private const float k_AnimationFadeDuration = 0.15f;


        private bool is_WindowOpen = false;

        private Select m_select = Select.None;

        public bool isSpawn = false;
        [SerializeField] private GameObject FunitureSpawner;
        /// <summary>
        /// The Game Object that provides feature points visualization.
        /// </summary>
        [Tooltip("The Game Object that provides feature points visualization.")]
        [SerializeField] private GameObject m_FeaturePoints = null;

        [SerializeField] private GameObject m_Buttons = null;



        [SerializeField] private Button m_SelectButtons = null;

        [SerializeField] private Button m_FloorButtons = null;

        [SerializeField] private Button m_FunitureButtons = null;

        [SerializeField] private Button m_WallButtons = null;

        [SerializeField] private Button m_ResetButtons = null;


        [SerializeField] private Button[] m_FloorProducts = null;

        [SerializeField] private Button[] m_FunitureProducts = null;

        [SerializeField] private Button[] m_WallProducts = null;

        [SerializeField] private Material[] m_FloorResoucres = null;

        [SerializeField] private GameObject[] m_FunitureResoucres = null;

        [SerializeField] private Material[] m_WallResoucres = null;

        [SerializeField] private GameObject m_WindowBackButton = null;

        [SerializeField] private GameObject m_SelectWindow = null;

        [SerializeField] private GameObject m_FloorWindow = null;
        [SerializeField] private GameObject m_FunitureWindow = null;
        [SerializeField] private GameObject m_WallWindow = null;

        /// <summary>
        /// The RawImage that provides rotating hand animation.
        /// </summary>
        [Tooltip("The RawImage that provides rotating hand animation.")]
        [SerializeField] private RawImage m_HandAnimation = null;

        /// <summary>
        /// The snackbar Game Object.
        /// </summary>
        [Tooltip("The snackbar Game Object.")]
        [SerializeField] private GameObject m_SnackBar = null;

        /// <summary>
        /// The snackbar text.
        /// </summary>
        [Tooltip("The snackbar text.")]
        [SerializeField] private Text m_SnackBarText = null;


        private Animation m_Win_Ani;

        private Material m_SelectMaterial;

        private GameObject m_SelectPrefab;
        /// <summary>
        /// The elapsed time ARCore has been detecting at least one plane.
        /// </summary>
        private float m_DetectedPlaneElapsed;

        /// <summary>
        /// The elapsed time ARCore has been tracking but not detected any planes.
        /// </summary>
        private float m_NotDetectedPlaneElapsed;

        /// <summary>
        /// Indicates whether a lost tracking reason is displayed.
        /// </summary>
        private bool m_IsLostTrackingDisplayed;

        /// <summary>
        /// A list to hold detected planes ARCore is tracking in the current frame.
        /// </summary>
        private List<DetectedPlane> m_DetectedPlanes = new List<DetectedPlane>();


        private void Awake()
        {
            if (instance)
            {
                DestroyImmediate(gameObject.GetComponent<PlaneManager>());
                return;
            }
            instance = this;
        }

        /// <summary>
        /// Unity's Start() method.
        /// </summary>
        public void Start()
        {

            m_select = Select.None;

            _CheckFieldsAreNotNull();
            m_SelectButtons.onClick.AddListener(_PressSelectButton);
            m_ResetButtons.onClick.AddListener(_PressReset);
            m_WindowBackButton.GetComponent<Button>().onClick.AddListener(_PressBackButton);
            m_FloorButtons.onClick.AddListener(() => _PressButton(Select.Floor));
            m_FunitureButtons.onClick.AddListener(() => _PressButton(Select.Furniture));
            m_WallButtons.onClick.AddListener(() => _PressButton(Select.Wall));
          
            m_IsLostTrackingDisplayed = false;
            m_NotDetectedPlaneElapsed = DisplayGuideDelay - k_OnStartDelay;
            m_Win_Ani = m_SelectWindow.GetComponent<Animation>();

        }

        /// <summary>
        /// Unity's OnDestroy() method.
        /// </summary>
        public void OnDestroy()
        {
            m_SelectButtons.onClick.RemoveListener(_PressSelectButton);
            m_ResetButtons.onClick.RemoveListener(_PressReset);
            m_WindowBackButton.GetComponent<Button>().onClick.RemoveListener(_PressBackButton);
            m_FloorButtons.onClick.RemoveListener(() => _PressButton(Select.Floor));
            m_FunitureButtons.onClick.RemoveListener(() => _PressButton(Select.Furniture));
            m_WallButtons.onClick.RemoveListener(() => _PressButton(Select.Wall));
          
        }

        /// <summary>
        /// Unity's Update() method.
        /// </summary>
        public void Update()
        {

            _UpdateDetectedPlaneTrackingState();
            _UpdateUI();
            //if (Input.touchCount > 0 && Input.GetTouch(0).phase == TouchPhase.Began)
            //{
            //    RaycastHit hit;
            //    Ray ray = Camera.main.ScreenPointToRay(Input.GetTouch(0).position);
            //    Physics.Raycast(ray, out hit);
            //    //Select Hool
            
            //    Debug.Log(hit.transform.name);
            //    te.text = hit.transform.name;
            //}
            if (m_select == Select.Floor || m_select == Select.Wall)
            {
                if (Input.touchCount > 0 && Input.GetTouch(0).phase == TouchPhase.Began
                    &&WindowClosed.Instance.IsClosed)
                {
                    RaycastHit hit;
                    Ray ray = Camera.main.ScreenPointToRay(Input.GetTouch(0).position);
                    Physics.Raycast(ray, out hit);
                    //Select Hool
                    hit.transform.GetComponent<MeshRenderer>().material = m_SelectMaterial;
                    //Debug.Log(hit.transform.name);
                    //te.text = hit.transform.name;
                }
            }
        }
        public Select GetSelect()
        {
            return m_select;
        }
        public void PressFloorProduct(int i)
        {
            m_SelectMaterial = m_FloorResoucres[i];
            _WindowClose();
        }
        public void PressFunitureProduct(int i)
        {
            isSpawn = true;
            m_SelectPrefab = m_FunitureResoucres[i];
            FunitureSpawner.GetComponent<AndyPlacementManipulator>().
                SetFuniturePrefab(m_SelectPrefab);
            _WindowClose();
           
        }
        public void PressWallProduct(int i)
        {
            m_SelectMaterial = m_WallResoucres[i];
            _WindowClose();
        }
      
        private void _PressSelectButton()
        {
            if (is_WindowOpen)
            {
                _WindowClose();
                return;
            }

            // open select window
            m_Win_Ani.Play("WindowOpen");
            is_WindowOpen = true;
            WindowClosed.Instance.IsClosed = false;
        }

        private void _PressButton(Select sel)
        {
            m_select = sel;
            m_Buttons.SetActive(false);
            m_WindowBackButton.SetActive(true);
            switch (m_select)
            {
                case Select.Floor:

                    m_FloorWindow.SetActive(true);
                    break;
                case Select.Furniture:
                    m_FunitureWindow.SetActive(true);
                    break;
                case Select.Wall:
                    m_WallWindow.SetActive(true);
                    break;
                default:

                    break;
            }

        }
        private void _PressBackButton()
        {
            m_WindowBackButton.SetActive(false);
            m_FloorWindow.SetActive(false);
            m_FunitureWindow.SetActive(false);
            m_WallWindow.SetActive(false);
            m_Buttons.SetActive(true);
        }
        private void _PressReset()
        {
            m_select = Select.None;


            m_NotDetectedPlaneElapsed = 0f;
            m_DetectedPlaneElapsed = 0f;
            m_SnackBar.SetActive(false);


        }

        private void _WindowClose()
        {
            m_Win_Ani.Play("WindowClose");
            is_WindowOpen = false;

            m_FloorWindow.SetActive(false);
            m_FunitureWindow.SetActive(false);
            m_WallWindow.SetActive(false);
            m_Buttons.SetActive(true);
        }

        /// <summary>
        /// Checks whether at least one plane being actively tracked exists.
        /// </summary>
        private void _UpdateDetectedPlaneTrackingState()
        {
            if (Session.Status != SessionStatus.Tracking)
            {
                return;
            }

            Session.GetTrackables<DetectedPlane>(m_DetectedPlanes, TrackableQueryFilter.All);
            foreach (DetectedPlane plane in m_DetectedPlanes)
            {
                if (plane.TrackingState == TrackingState.Tracking)
                {
                    m_DetectedPlaneElapsed += Time.deltaTime;
                    m_NotDetectedPlaneElapsed = 0f;
                    return;
                }
            }

            m_DetectedPlaneElapsed = 0f;
            m_NotDetectedPlaneElapsed += Time.deltaTime;
        }

        /// <summary>
        /// Hides or shows the UI based on the existence of a plane being currently tracked.
        /// </summary>
        private void _UpdateUI()
        {
            if (Session.Status == SessionStatus.LostTracking &&
                Session.LostTrackingReason != LostTrackingReason.None)
            {
                // The session has lost tracking.
                m_FeaturePoints.SetActive(false);
                m_HandAnimation.enabled = false;
                m_SnackBar.SetActive(true);
                switch (Session.LostTrackingReason)
                {
                    case LostTrackingReason.InsufficientLight:
                        m_SnackBarText.text = "공간이 너무 어두워요";
                        break;
                    case LostTrackingReason.InsufficientFeatures:
                        m_SnackBarText.text = "카메라를 색이 있는 공간에 향하세요.";
                        break;
                    case LostTrackingReason.ExcessiveMotion:
                        m_SnackBarText.text = "움직임이 너무 빨라요.";
                        break;
                    default:
                        m_SnackBarText.text = "인식이 안돼요.";
                        break;
                }


                m_IsLostTrackingDisplayed = true;
                return;
            }
            else if (m_IsLostTrackingDisplayed)
            {
                // The session has moved from the lost tracking state.
                m_SnackBar.SetActive(false);
                m_IsLostTrackingDisplayed = false;
            }

            if (m_NotDetectedPlaneElapsed > DisplayGuideDelay)
            {
                // The session has been tracking but no planes have been found by
                // 'DisplayGuideDelay'.
                m_FeaturePoints.SetActive(true);

                if (!m_HandAnimation.enabled)
                {
                    m_HandAnimation.GetComponent<CanvasRenderer>().SetAlpha(0f);
                    m_HandAnimation.CrossFadeAlpha(1f, k_AnimationFadeDuration, false);
                }

                m_HandAnimation.enabled = true;
                m_SnackBar.SetActive(true);

                if (m_NotDetectedPlaneElapsed > OfferDetailedInstructionsDelay)
                {
                    //  m_SnackBarText.text = "Need Help?";

                }
                else
                {   // 카메라를 인식하고 싶은 곳에 향하세요.
                    m_SnackBarText.text = "카메라를 인식하고 싶은 곳에 향하세요.";

                }
            }
            else if (m_NotDetectedPlaneElapsed > 0f || m_DetectedPlaneElapsed > k_HideGuideDelay)
            {
                // The session is tracking but no planes have been found in less than
                // 'DisplayGuideDelay' or at least one plane has been tracking for more than
                // 'k_HideGuideDelay'.
                m_FeaturePoints.SetActive(false);
                m_SnackBar.SetActive(false);


                if (m_HandAnimation.enabled)
                {
                    m_HandAnimation.GetComponent<CanvasRenderer>().SetAlpha(1f);
                    m_HandAnimation.CrossFadeAlpha(0f, k_AnimationFadeDuration, false);
                }

                m_HandAnimation.enabled = false;
            }
        }

        /// <summary>
        /// Checks the required fields are not null, and logs a Warning otherwise.
        /// </summary>
        private void _CheckFieldsAreNotNull()
        {


            if (m_SnackBarText == null)
            {
                Debug.LogError("SnackBarText is null");
            }

            if (m_SnackBar == null)
            {
                Debug.LogError("SnackBar is null");
            }


            if (m_HandAnimation == null)
            {
                Debug.LogError("HandAnimation is null");
            }

            if (m_FeaturePoints == null)
            {
                Debug.LogError("FeaturePoints is null");
            }
        }
    }

}