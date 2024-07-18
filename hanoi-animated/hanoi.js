let scene, camera, renderer, controls;
let rods = { A: [], B: [], C: [] };
let diskMeshes = [];
let steps = [];
let stepIndex = 0;
let animationInProgress = false;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.25;
    controls.enableZoom = true;

    createRods();
    createDisks(3);  // Change this number to the desired number of disks

    camera.position.z = 10;
    animate();
}

function createRods() {
    const rodGeometry = new THREE.CylinderGeometry(0.1, 0.1, 6, 32);
    const rodMaterial = new THREE.MeshBasicMaterial({ color: 0xaaaaaa });

    ['A', 'B', 'C'].forEach((label, index) => {
        const rodMesh = new THREE.Mesh(rodGeometry, rodMaterial);
        rodMesh.position.x = (index - 1) * 4;
        rodMesh.position.y = -1;
        scene.add(rodMesh);
    });
}

function createDisks(n) {
    const colors = [0xff0000, 0x00ff00, 0x0000ff, 0xffff00, 0xff00ff, 0x00ffff, 0xffffff];
    for (let i = 0; i < n; i++) {
        const diskGeometry = new THREE.CylinderGeometry(0.5 - i * 0.1, 0.5 - i * 0.1, 0.2, 32);
        const diskMaterial = new THREE.MeshBasicMaterial({ color: colors[i % colors.length] });
        const diskMesh = new THREE.Mesh(diskGeometry, diskMaterial);
        diskMesh.position.y = i * 0.25 - 0.5;
        diskMesh.position.x = -4;
        scene.add(diskMesh);
        rods.A.push(diskMesh);
        diskMeshes.push(diskMesh);
    }
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

function hanoi(n, source, auxiliary, target) {
    if (n > 0) {
        hanoi(n - 1, source, target, auxiliary);
        steps.push([source, target]);
        hanoi(n - 1, auxiliary, source, target);
    }
}

function startHanoi() {
    if (!animationInProgress) {
        steps = [];
        document.getElementById('steps').innerHTML = '';
        hanoi(rods.A.length, 'A', 'B', 'C');
        displaySteps();
        stepIndex = 0;
        animationInProgress = true;
        executeSteps();
    }
}

function executeSteps() {
    if (stepIndex < steps.length) {
        const [from, to] = steps[stepIndex];
        moveDisk(from, to);
        stepIndex++;
        setTimeout(executeSteps, 1000); // Change the delay as needed
    } else {
        animationInProgress = false;
    }
}

function moveDisk(from, to) {
    const disk = rods[from].pop();
    const toRod = rods[to];
    const newY = toRod.length * 0.25 - 0.5;
    disk.position.set((to === 'A' ? -4 : to === 'B' ? 0 : 4), newY, 0);
    toRod.push(disk);
}

function displaySteps() {
    const stepsContainer = document.getElementById('steps');
    steps.forEach(([from, to], index) => {
        const stepElement = document.createElement('div');
        stepElement.textContent = `Step ${index + 1}: Move disk from ${from} to ${to}`;
        stepsContainer.appendChild(stepElement);
    });
}

const restartHanoi = () => {  
    if (animationInProgress) {
        animationInProgress = false;
    }
    stepIndex = 0;
    rods = { A: [], B: [], C: [] };
    diskMeshes.forEach(mesh => {
        mesh.position.set(-4, mesh.position.y, 0);
        rods.A.push(mesh);
    });
}

init();
